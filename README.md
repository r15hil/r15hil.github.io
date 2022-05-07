# r15hil.github.io
 
Run build.sh to generate the site.
When adding a new component, add the following, to generate md files which include imports:
```
markdown-pp foo.mdpp -o foo.md
```
To maintain the structure of the site, each component must include 

> foo.mdpp

and

>foo-embed.md

The *foo-embed.md* contains the contents of the component as well as serving the expand box feature, whereas *foo.mdpp* will be the standalone page which uses MarkdownPP and serves as the standalone content (not expand box).