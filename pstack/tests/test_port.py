import json,os,pathlib,subprocess,tempfile,unittest,yaml
ROOT=pathlib.Path(__file__).resolve().parents[1]
class PortTests(unittest.TestCase):
 def test_package(self):
  skills=list(ROOT.glob('skills/*/SKILL.md'));self.assertEqual(len(skills),65)
  self.assertEqual(len(list(ROOT.rglob('SKILL.md'))),65)
  for p in skills:
   meta=yaml.safe_load(p.read_text().split('---',2)[1]);self.assertEqual(meta['name'],p.parent.name)
   self.assertEqual((p.parent/'references/chatgpt.md').read_text(),(ROOT/'docs/harness/chatgpt.md').read_text())
  for p in (ROOT/'automations').rglob('*.md'):self.assertNotIn('SKILL.md',p.read_text())
  for p in (ROOT/'skills/poteto-mode').rglob('*.md'):self.assertNotIn('/deslop',p.read_text())
  for p in [ROOT/'plugin.json',ROOT/'.codex-plugin/plugin.json']:
   self.assertEqual(json.loads(p.read_text())['version'],'0.16.1')
 def test_cleanup(self):
  with tempfile.TemporaryDirectory() as temp:
   d=pathlib.Path(temp); repo=d/'repo';repo.mkdir();bindir=d/'bin';bindir.mkdir()
   for name in ['gh','origin']:
    p=bindir/name;p.write_text('#!/bin/sh\nexit 1\n');p.chmod(0o755)
   env={**os.environ,'PATH':str(bindir)+os.pathsep+os.environ['PATH']}
   def git(*args):return subprocess.run(['git','-C',str(repo),*args],check=True,capture_output=True,text=True,env=env)
   git('init','-b','main');git('config','user.email','test@example.invalid');git('config','user.name','Test')
   (repo/'tracked').write_text('base');(repo/'.gitignore').write_text('private-data\n')
   git('add','.');git('commit','-m','base')
   expected={'clean space':'verify-unused','untracked':'hold-data','ignored':'hold-data','tracked':'hold-wip','unmerged':'review'}
   for name in expected:
    wt=d/name;git('worktree','add','-b',name.replace(' ','-'),str(wt))
    if name=='untracked':(wt/'important-source.py').write_text('valuable source')
    if name=='ignored':(wt/'private-data').write_text('valuable ignored data')
    if name=='tracked':(wt/'tracked').write_text('unfinished edit')
    if name=='unmerged':
     subprocess.run(['git','-C',str(wt),'commit','--allow-empty','-m','unique'],check=True,capture_output=True)
   out=subprocess.run(['bash',str(ROOT/'skills/poteto-mode/scripts/worktree-audit.sh'),'-b','main',str(repo)],capture_output=True,text=True,check=True,env=env).stdout
   rows={pathlib.Path(a[-1]).name:a for line in out.splitlines() if not line.startswith(('#','SIZE')) and len(a:=line.split('\t'))==9}
   for name,bucket in expected.items():self.assertEqual(rows[name][7],bucket,out)
   self.assertEqual((d/'untracked/important-source.py').read_text(),'valuable source')
   self.assertEqual((d/'ignored/private-data').read_text(),'valuable ignored data')
   print(out)
if __name__=='__main__':unittest.main()
