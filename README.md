# AU School Handwriting Fonts

The AU School Handwriting Fonts are a variable typeface family designed specifically to meet Australian education standards. While carefully crafted to work well in a classroom environment, the fonts are handy outside the classroom as well.

The initial weight of these English language font-sets is intended to imitate the pencil thickness of actual handwriting, however they may be adjusted as desired in your usual word processor, or they can be used in software that supports Open Type Fonts (such as Adobe) to make full use of alternate glyphs for transitional handwriting stages between grades 1 and 3.


- - - -

![sample 001](https://user-images.githubusercontent.com/34974280/174480772-0263a627-f43b-49bd-9ca0-935cd7906826.png)

- - - -

The AU School Handwriting Fonts are purposefully designed with minimal under and over shoot at Cap Height, X-Height, Baseline and Descender, making them perfect for use by teachers.

- - - -

## Description ##

In lower primary school some Australian States teach different handwriting styles, while some States share the same style. The "documentation" subdirectories contain PDF's for each State's style requirements, along with proofs to inspect the font before downloading it.

The handwriting styles expected by each State's Education Department are summarized as follows:

State | Year 1 to 2/3 | Year 3/4+ | Alts | SMC | Link
| :--- | :--- | :--- | :--- | :--- | :---
Queensland (QLD)  | QBeginners Print | QBeginners Precursive | [x] | [x] | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/QLD-School-Fonts "Read more")
New South Wales (NSW) | Foundation Print | Foundation Precursive | [x] | [x] | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/NSW-ACT-School-Fonts "Read more")
Tasmania (TAS) | Beginner Print | Precursive Print | [x] | [ ] | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/TAS-School-Fonts "Read more")
Australian Capital Territory (ACT) | Foundation Print | Foundation Precursive | [x] | [ ] |  [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/NSW-ACT-School-Fonts "Read more")
Victoria (VIC) | Print | Infant Cursive | [x] | [ ] | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/VIC-WA-NT-School-fonts "Read more")
Northern Territory (NT) | Print | Infant Cursive | [x] | [ ] | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/VIC-WA-NT-School-fonts "Read more")
Western Australia (WA) | Print | Infant Cursive | [x] | [ ] | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/VIC-WA-NT-School-fonts "Read more")
South Australia (SA) | Beginner Print | Precursive Print | [x] | [ ] | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/SA-School-Fonts "Read more")

```
Alts: Denotes whether [x] or not [ ] the transitional precursive alternate glyphs have been included.
SMC: Denotes whether [x] or not [ ] small caps glyphs have been included.
```

- - - -

## View and/or Install the Fonts ##

To view the fonts without installing them:

<details>
   <summary>Click here</summary>

Click the link above matching the Australian State that you live in. 

1. Download the font-viewer.zip file and unpack it. 
2. Double-click the .html file.
3. Adjust the sliders at the top of the page.

![Font Viewer](https://user-images.githubusercontent.com/34974280/174448031-b3235cea-d3f9-4194-9a05-d9e2d5585775.png)
</details>

To install the fonts choose an option:

<details>
  <summary>Windows</summary>

1. Open the *Windows Control Panel*
2. Select *Appearance and Personalization*
3. At the bottom, select *Fonts*
4. To add a font, simply drag the .ttf file into the font window.
5. Click Click Yes when prompted.

</details>
<details>
  <summary>Mac</summary>

1. Double-click the .ttf file
2. Click Install Font in the font preview window
3. After validation, it will open in the Font Book app

</details>

- - - -

# About This Project #

This project contains the binary font files for all Australian states. Each family's subdirectory contains the .ttf font file sets, the source files and a .zip file to locally test the font in a variable font viewer without installing.

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

## Ongoing & Future Development ##

Some transitional precursive alternate glyph-sets are still under development, along with some small caps. Common math symbols used by Years 1 to 4 have been included in all sets. Advanced math symbols will come along with future development.

The full cursive counterparts (for years 4-5 onward) will be developed in due course, using a different software package designed specifically for cursive fonts in school/teaching environments.

- - - -

# Acknowledgements & Credits #

Thanks to "Google for Education" for supporting little Australian schoolies and making these fonts widely and freely avaible to everyone. The following contributors made this project happen, their hard work is muchly appreciated!

- Santiago Orozco (Typefacing Intricacies)
- David Berlow (Production Manager)
- Rosalie Wagner (Final Proofs and Product Output)
- Corey Anderson (Calligraphy Artist)
- Tina Anderson (Font Design)

- - - -

# Changelog #

**2022 Version 1.001**

Date          | Description
------------- | -------------
Jan 10        | Initial commit
Jun 18        | First release

- - - -

# License #

Copyright (c) 2022 The AU School Handwriting Fonts Project Authors (https://github.com/MezMerrit/AU-School-Handwriting-Fonts)

These Fonts are licensed under the SIL Open Font License, Version 1.1. This license is copied [here](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/blob/main/OFL.txt "SIL Open Font License"), and is also available with a FAQ at: (https://scripts.sil.org/OFL).

The fonts files themselves also contain licensing and authorship metadata.

- - - -

# Repository Layout #

This font repository structure is inspired by [Unified Font Repository v0.3](https://github.com/unified-font-repository/Unified-Font-Repository), modified for the [Google Fonts workflow](https://github.com/googlefonts/googlefonts-project-template).
