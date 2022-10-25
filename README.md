# AU School Handwriting Fonts

The AU School Handwriting Fonts are an English language, OpenType, variable typeface family designed specifically to meet Australian Education standards.  While weights, widths and optical sizes were carefully crafted to work well in an Australian classroom environment, they are just as comfortable to read and work with in the home environment. 

AU School Handwriting Fonts ranges in weights from 400 to 700, making them useful for print media as well. Default versions of the fonts come with OpenType features to aid in transitional stages between learning basic handwriting to the initial cursive stage. Each font contains every possible character produced by an English language keyboard, including common math symbols used by Australian students from Years 1 to 4.

Google Workspace users are provided standard versions online, however they may download or build the complete OpenType versions from GitHub for local installations.

- - - -

![sample](https://user-images.githubusercontent.com/34974280/174619693-326823ef-5541-4aa9-a538-301661f3a1d6.png)

- - - -

## Description ##

In lower primary school some Australian States teach different handwriting styles, while some States share the same style. The "documentation" subdirectories contain PDF's for each State's style requirements.

The handwriting styles expected by each State's Education Department are summarized as follows:

State | Year 1 to 2/3 | Base | Year 3/4+ | Alts | SMC | Link
| :--- | :--- | :---: | :--- | :--- | :--- | :---
New South Wales (NSW) | Foundation Manuscript | ✅ | Foundation Precursive | ✅ | ✅ | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/NSW-ACT-School-Fonts "Read more")
Australian Capital Territory (ACT) | Foundation Print | ✅ | Foundation Precursive | ✅ | ✅ |  [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/NSW-ACT-School-Fonts "Read more")
Queensland (QLD) | QBeginners Print | ✅ | QBeginners Precursive | ❌ | ✅ | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/QLD-School-Fonts "Read more")
South Australia (SA) | Beginner Print | ✅ | Precursive Print | ❌ | ❌ | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/SA-School-Fonts "Read more")
Tasmania (TAS) | Beginner Print | ✅ | Precursive Print | ❌ | ❌ | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/TAS-School-Fonts "Read more")
Victoria (VIC) | Label Print | ✅ | Infant Cursive | ❌ | ❌ | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/VIC-WA-NT-School-fonts "Read more")
Western Australia (WA) | Label Print | ✅ | Infant Cursive | ❌ | ❌ | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/VIC-WA-NT-School-fonts "Read more")
Northern Territory (NT) | Label Print | ✅ | Infant Cursive | ❌ | ❌ | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/VIC-WA-NT-School-fonts "Read more")

```
Base: Denotes the basic print version of the font.
Alts: Denotes whether ✅ or not ❌ the precursive alternate glyphs are currently included.
SMC: Denotes whether ✅ or not ❌ small caps glyphs are currently included.

* Additions will be made to this guide as they are completed and the fonts are updated.
```

- - - -

## Features ##

The regular weight of the font family is intended to imitate the pencil thickness of actual handwriting, however the scalability of the fonts enables them to be widely varied according to intended usage.

The fonts can also be used in software that supports OpenType Fonts (such as Adobe products, MS Word or Mac's native Pages app) to make full use of alternate glyphs for precursive variations (as shown below).

![opentype-ani](https://user-images.githubusercontent.com/34974280/174490884-cc6b3630-c1d4-4711-b878-0ff5e73a1cf2.gif)

![msword-demo](https://user-images.githubusercontent.com/34974280/197845580-0026e7f5-263a-48c8-8a75-34bde86830ae.gif)

Additionally, AU School Handwriting Fonts are purposefully designed with minimal under and over shoot at Cap Height, X-Height, Baseline and Descender, making them perfect for use by teachers. Adjusting the fonts to fit dotted thirds pre-ruled mediums can be achieved using Adobe products.

Also provided here is watermarks.zip containing dotted-thirds, plain-thirds and regular-rule images that may be used in any word processor that supports watermarks (example below is Mac's Pages app using Image Fill or Advanced Image Fill).

![pages-watermark](https://user-images.githubusercontent.com/34974280/176444108-ea7e5d84-6b28-44dd-bc3f-6b13680e6026.gif)

By adjusting the scaling of the watermark image, the document's top margin and line spacing as well as the font size, almost any type of ruled page can be produced.

- - - -

## Ongoing & Future Development ##

Some transitional precursive alternate glyph-sets are still under development, along with some small caps. The full cursive counterparts (for years 4-5 onward) are under way, along with Outline, Outline Arrows and Dotted variations.

Watch the table above for progress notification.

- - - -

# About This Project #

This project contains the binary font files for all Australian states. 

Each family's subdirectory contains .ttf font file sets, as well as .glyphs source files. 

Standard installation instructions are provided above, otherwise instructions for the build tools are provided below.

- - - -

## Build from gftool ##

Fonts are built automatically by GitHub Actions - look under the "Actions" tab for the latest build.

You can also build the font locally, after cloning this repository.

```
1. At the root of your local clone (cd path/to/local/clone), create a virtual environment: python3 -m venv env

2. Activate the virtual env: source env/bin/activate

3. Install gftools (or the requirements) in the virtual env: pip install gftools

4. go to the "sources" directory and from the terminal, run : gftools builder config.yaml
```

- - - -

## Bugs & Improvements ##

These fonts are the result of a collaborative project, where you are invited to discuss issues and even contribute to their ongoing development by way of suggestions.

If you find a problem with a font file or have a request for the future development of its cursive counterpart, [please create a new issue in this project's issue tracker](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/issues "Go to the issue tracker").

- - - -

# Credits #

### Typeface Artist ###
- Corey Anderson

### Typeface Designer ###
- Tina Anderson

### Team Leads ###
- Eben Sorkin (Sorkin Type Co)
- David Berlow (The Font Bureau, Inc)
- Dave Crossland (Google Fonts)
- Chris Betcher (Google for Education)

### Typeface Engineers ###
- Rosalie Wagner (Google Fonts)
- Santiago Orozco (The Font Bureau, Inc)

- - - -

# Fontlog #

**2022 Version 1.001**

Date          | Description
------------- | -------------
Jan 10        | Initial commit
Apr 10        | Submitted designs for all precursive sets
Jun 18        | First release
Jun 20        | Reset initial font sizes to 11pt
Jun 23        | Adjusted linespacing for print mediums

* Refer to each font's ReadMe for further updates.

- - - -

# License #

Copyright (c) 2022 The AU School Handwriting Fonts Project Authors (https://github.com/MezMerrit/AU-School-Handwriting-Fonts)

These Fonts are licensed under the SIL Open Font License, Version 1.1. This license is copied [here](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/blob/main/OFL.txt "SIL Open Font License"), and is also available with a FAQ at: (https://scripts.sil.org/OFL).

The fonts files themselves also contain licensing and authorship metadata.

- - - -

# Repository Layout #

This font repository structure is inspired by [Unified Font Repository v0.3](https://github.com/unified-font-repository/Unified-Font-Repository), modified for the [Google Fonts workflow](https://github.com/googlefonts/googlefonts-project-template).
