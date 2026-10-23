# pstack-chatgpt

Maintained translation of pstack into a ChatGPT plugin.

This repository contains the ChatGPT adaptation of [Lauren Tan’s pstack](https://github.com/cursor/plugins/tree/main/pstack). The plugin source is in `pstack/`, currently version **0.16.1**, with 65 skills covering engineering investigation, adversarial review, verification, writing, and native agent workflows.

## Install your own copy

1. Download or clone this repository.
2. From its root, run `python tools/package.py` with Python 3. This creates `dist/pstack-0.16.1.zip`.
3. Attach that ZIP in ChatGPT with Plugin Creator selected and ask: “Create a private plugin from this package.” Plugin Creator must be available in your account.
4. Select the resulting plugin and ask to use `setup-pstack`, `poteto-mode`, `interrogate`, or `unslop`.

Each installation is an independent copy. Repository updates do not automatically update installed plugins. To update your copy, build a fresh ZIP and ask Plugin Creator to update the existing plugin, preserving its identity and settings. The maintainer’s private plugin link and weekly automation do not grant access or configure automation in other accounts.

## Native workflows

| Task | Skill |
| --- | --- |
| GitHub PR review | `pr-review` |
| Bounded continuation and requested schedules | `resume-work` |
| Report intake and classification | `triage-reports` |
| Reproduction and tested fixes | `reproduce-fix` |
| Agent delegation | `delegate-work` |
| Requested model-role choices | `configure-models` |
| Repository guidance | `project-defaults` |
| GitHub operations | `github-workflow` |
| History and handoffs | `recall` |

Available host tools determine what can run. Most skills require explicit invocation. Installing the package does not start subscriptions, connect services, or authorize external writes. Historical Benny files are reference material.

## Verify

With Python 3 and PyYAML installed, run:

```sh
python -m unittest discover -s pstack/tests -v
```

Five package and cleanup tests passed for this release. See [the verification record](pstack/docs/verification.md) for local reproduction evidence and the limits of live integration testing. Static instruction checks do not establish runtime enforcement.

## Source and license

The plugin is adapted from upstream commit `8b3326d99fd4b993cb33a24dad8af03175c642c5`, pstack version 0.15.30. See [the native guide](pstack/docs/guide/README.md) and [plugin README](pstack/README.md).

The repository’s MIT license is preserved in [LICENSE](LICENSE). Upstream pstack attribution and MIT terms remain in [pstack/LICENSE](pstack/LICENSE). The ChatGPT release version is maintained independently of the upstream version.
