# Local development

Use this directory for temporary previews, generated media, logs, validation
reports and working notes. Everything here except this README is ignored by Git
and is not included in a fresh clone. Keep any needed local backups separately.

The current showcase preview is in `showcase_preview_20261010/`. From the
repository root, serve it with:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory development/showcase_preview_20261010
```

Open <http://localhost:8765/research.html> for the Research-page draft or
<http://localhost:8765/> for the review overview. Read the preview's
`HANDOFF_PROMPT.md` before editing. Its generator can overwrite hand-edited
wording, so do not rebuild it without first inspecting the current files.

Website integration and publication require explicit acceptance. Once accepted,
integrate page content through root `build.py` and selected media through
`assets/`, following the repository's source-and-generated-HTML workflow.
Do not force-add the preview package to publish it.
