# Uploading Blogs - 2023

### STEP 1 : 
- Clone the `blogs-2023` branch.
- `cd scripts`
- copy the markdown file of the blog you are uploading to the scripts directory and rename it to `blog.md`.
- copy the images required for the blog into `images/` folder in the scripts directory.
- add the author images with their names into the same `images/` folder.
- The Final directory should look something like this :
    - scripts/
       - uploadBlog.py
       - blog.md
       - images/
           - image1.jpg  
           - image2.jpg  
           - image3.png  
           - image4.svg  
           - authorname1.jpg  
           - authorname2.jpg

### STEP 2 :  
- Ensure the markdown file is free of errors and in correct md format.
- Make sure the images mentioned in the markdown file match the ones in the folder (along with their extensions).
- Make sure links are properly mentioned with https:// prefix, remove redundant braces wherever found.
- Remove any unnecessary quotations from the blog title / description

### STEP 3 :
- run the script : `python uploadBlog.py blogtoupload.md`
- Depending on the number of authors the script will ask you to enter the author details i.e Name, Email and the name of their author image in the `images/` folder.
- After inserting everything, the script will automatically make necessary folders for images, appropriate renamings and will add the author info into the authors.yml file.

### STEP 4 :
- `jekyll serve` and ensure the blog is correctly displayed.
- Create a Pull request from your `clone/blogs-2023` to  `IEEE-NITK/blog/blogs-2023`
- Fix any errors displayed by the HTMLProofer
- Request review
