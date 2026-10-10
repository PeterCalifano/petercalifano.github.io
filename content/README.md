# Editing the website text

Edit the text files below, then run `python3 build.py` from the repository root.
The build regenerates the HTML pages. Do not edit generated HTML directly.

| File | Content |
| --- | --- |
| [home.md](home.md) | Homepage role, lead, About paragraph and research highlight |
| [research.md](research.md) | Research introduction and bullet lists |
| [projects.md](projects.md) | Mission and software descriptions |
| [about.md](about.md) | Background introduction, experience, education and skills |
| [beyond.md](beyond.md) | Personal interests and quotations |
| [publications.json](publications.json) | Publication records |

Keep the `##` section names: the builder uses them to find each piece of text.
They are editing labels; changing their order does not change the page layout.
Write ordinary text below them, without Python quotes or HTML tags.
The `<!-- ... -->` comments explain where each section appears. They are ignored
by the builder and never appear in the generated pages. You can edit or add them.

- Wrap long sentences across lines as you prefer. They render as one paragraph.
- In the homepage About section and mission/education descriptions, a blank line
  starts a new paragraph. Introductions, role labels, software cards, experience,
  skill and hobby descriptions are single text fields; blank lines there are folded.
- In research sections, start each bullet with `- `. Continue a long bullet on
  an indented line. Add or remove bullets by adding or removing those lines.
- Use `*italics*` for titles in hobby descriptions and other formatted text fields.
  Software cards, experience and skills are plain text.
- Write `&`, apostrophes and accented characters normally. HTML is escaped.

This is a small Markdown subset: paragraphs, bullet lists and italics. Tables,
images, embedded HTML and Markdown links are not interpreted. Navigation, section
titles, tags, dates, links and media placement remain in `build.py`.

Commit the edited Markdown files and the regenerated HTML together. To check the
builder and the editing format, run `python3 -m unittest discover -s tests`.
