# Pietro Califano · personal website

A professional, multipage site for research, publications, projects, background, and interests. Hosted at https://petercalifano.github.io/ using GitHub Pages.

## Update the site

Edit the Markdown files in `content/` for page text. Start with
[content/home.md](content/home.md) for the homepage About paragraph or
[content/research.md](content/research.md) for research bullets.
See the [editing guide](content/README.md) for the supported format.

Edit `build.py` for layout, section titles, dates and links; edit `assets/site.css`
or `assets/home.css` for styling. Publication records live in
`content/publications.json`. Run:

```sh
python3 build.py
```

Commit both the sources and generated HTML. The site works without JavaScript, package installation, or third-party fonts. All generated pages and assets are served from the repository root. `.nojekyll` disables Jekyll processing. GitHub Pages should publish the root of `main`.

## Local development previews

Keep temporary previews and generated review artifacts under `development/`.
Only its [development guide](development/README.md) is tracked; preview packages
remain local until accepted for integration into the website.

## Editorial style

Use neutral, subject-focused prose. Use third person for the short biography and direct action verbs for individual contributions. Avoid first-person narration outside attributed quotations, promotional slogans, filler introductions, and formulaic contrasts. Keep technical claims specific and distinguish personal contributions from project descriptions. Preserve the owner's original mottos as quotations. Keep sibling project descriptions at a consistent level: purpose and main method or contribution. Do not mix research areas with implementation features. Repository labels describe broad topics rather than availability. Verify external fragment identifiers against the destination page.

## Publication links

Publication record links use labels determined by entry type, regardless of the hosting provider:

- `Journal`: **Publication record**.
- `Conference`: **Conference record**.
- `Dataset` (for future entries): **Dataset record**.

Omit `url` when a public record is not yet available; the entry then renders without a link. Do not substitute conference programmes or generic event pages for paper records. Labels are defined centrally in `build.py`, without per-entry overrides.

## Project links

Use **Repository** for public software repositories, **Project page** for mission information, and **All repositories** for the GitHub repository listing. Software cards without a public repository show **Currently not published** as plain text; do not substitute research or facility links.

## Tags

Choose tags from [content/tags.json](content/tags.json), the shared catalogue for Research and Projects. The build rejects unknown or duplicate tags. Catalogue groups are for editing; tags appear together on the site.

- Use two to four relevant tags per item, based on its description and verified implementation. Do not add tools merely because they appear in the author's general skill list.
- Prefer methods or topics first, then supporting tools or hardware. Do not repeat a broad topic solely because it is already the card heading.
- Use one concept per tag: `MATLAB` and `C++`, not `MATLAB / C++`; `ONNX` and `TensorRT`, not `ONNX / TensorRT`.
- Use `C++` as the tag; retain language versions in technical descriptions. Preserve product names such as `ROS 2` and `MoveIt 2`.
- Use `Event-based vision` for the topic, `Machine learning inference` for inference, and `Model deployment` for deploying trained models.
- Preserve meaningful specificity: `SLAM` covers general SLAM tools; `Visual SLAM` identifies vision-based methods. `Navigation filtering` and `Recursive filtering` describe different scopes and are not interchangeable.
- Add a new catalogue entry only when an existing tag cannot accurately describe the item. Keep availability and publication status out of tags.

The initial review separated combined language/tool tags, normalized `C++20` to `C++`, replaced the event-camera topic label with `Event-based vision`, and clarified the inference/deployment labels. Page headings and publication types are separate from this catalogue.

## Page structure

- Home: brief About section and a compact experience timeline linking to detailed entries.
- Background: full appointments, education, and technical skills.
- Research: research methods, applications, and evaluation.
- Projects: mission contributions and concrete software or facilities.
- Publications: bibliographic records and manuscript status.
- Beyond work: personal interests and original mottos.

The homepage About/timeline arrangement takes inspiration from https://antoniorizza.github.io/; its text and implementation are original. Keep homepage summaries brief and avoid copying full descriptions between pages.

## Source records

Content was reviewed on 19 September 2026 against the updated `PeterCalifano/curriculum-vitae-builder` repository (claims, long CV, identity, and publication data), the live `PeterCalifano/PeterCalifano` profile README, DART's member page, and Politecnico publication records.

- CV claims blob: `3268576ff3428e6038edf7dbccef289a46c8f28e`
- Long CV blob: `a1940b2df3f2aa0203a483d5cdaece1dfb1e03cd`
- Publication data blob: `2dcd37e27831c0b5959bbaa0f4bf76779215bcd3`
- Identity blob: `7cb9be350f4f56d7aa624026e8159f9e9c4528a1`
- Profile: https://github.com/PeterCalifano
- DART: https://dart.polimi.it/member/?p=pietro+califano
- ASTRA paper: https://hdl.handle.net/11311/1307430
- LinkedIn: https://www.linkedin.com/in/pietro-califano-a46b7b199/

The LinkedIn URL was confirmed by the owner. Its content could not be fetched, so no LinkedIn-only claims were imported. The owner explicitly requested the hobbies shown. The portrait is from the CV repository. The updated CV places DFKI in Milan; the site omits that location pending clarification. Manuscripts are separated from published work. Publication author lists abbreviated as “et al.” are retained from the CV; no missing coauthors or DOIs were invented.

The biography and current research status require periodic review. No automatic CV synchronization is configured.

## Research showcase media

The Research page loads Bennu, Apophis and Itokawa media from the
[Research showcase media release](https://github.com/PeterCalifano/petercalifano.github.io/releases/tag/research-showcase-2026-10-10).
Videos, the tracking GIF and video posters are release attachments, not Git
objects. `RESEARCH_MEDIA` in `build.py` sets their versioned URL. Keep the
attachment names stable; use a new release tag when replacing the media.

Temporary renders, replay frames, source manifests and review pages remain in
the ignored `development/` directory. Regenerate `research.html` with the normal
site build after changing its source.
