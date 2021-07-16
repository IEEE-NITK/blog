# Contributing guidelines
### Step 1: Fork this repository and clone it
- Install git if you don't have it. Here's an [article](https://www.digitalocean.com/community/tutorials/how-to-contribute-to-open-source-getting-started-with-git) on how to install git on Windows/Linux/macOS
- Fork the [blog repository](https://github.com/IEEE-NITK/blog) and clone it.
If you're not sure how to fork or clone a repository, refer to [this](https://www.digitalocean.com/community/tutorials/fork-clone-make-changes-push-to-github) article or do some googling on your own, or ask someone on our Slack workspace under the #github channel.
### Step 2: First-time authors
If you're not a first time author, feel free to skip to the next section.

- Add your image to the `assets/img/authors` folder and make sure you have a square image.  
- Open the file `_data/authors.yml` and add your details at the end of the file in the following format:
  ```
  <your-github-username>:
  	name: <your-name>
  	github: <your-github-username>
	author_image: <filename-of-the-image-you-added>
	description: <a-descrtiption-of-your-choice>
	email: <your-email>
  ```
### Step 3: Adding the post
- Create a new `.md` file in the `_posts` folder and name it in the following format:
	`year-month-date-title-of-your-choice.md`
- Add content to your new post in markdown syntax. Refer to [this](https://guides.github.com/features/mastering-markdown/) link about Github's flavor of markdown or try googling it if you're not familiar with markdown. Here's an example: 
	```
	---
	layout: post
	title: "Writing a sample blog"
	author_github: githubuser123
	date: 2017-05-14 23:32:44
	image: '/assets/img/'
	description: 'Introductory post on writing a blog'
	tags:
	- IEEE NITK
	- Blog
	categories:
	- CompSoc/Diode/Piston
	github_username: 'githubuser123'
	---
	GraphQL is a query language for APIs and a runtime for fulfilling those queries 
	with your existing data. 
	GraphQL provides a complete and understandable description of the data in your API,
	gives clients the power to ask for exactly what they need and nothing more,
	makes it easier to evolve APIs over time, and enables powerful developer tools.
	```
- A post consists of the <b>head</b> and the <b>body</b>:
	#### Head:
	- layout :  should always be set to "post"
	- title : title of your post 
	- author_github :  your github username 
	- date :  today's date in the format '2020-04-25 17:30:30 '
	- image : location of the images, should always be set to 'assets/img/' 
	- description : a description of your post 
	- tags :  post tags 
	- categories : categories your post belongs to
	- github_username : your github username
	#### Body:
	- This is where your content goes. In Github's flavor of markdown.

### Step 4: Build locally and check for errors
 - Install [Ruby and Jekyll](https://jekyllrb.com/docs/installation/)
 - Install other dependencies:
 	```
 	gem install html-proofer jekyll-paginate jemoji
 	```
 - Then build your blog:
 	```
	jekyll build --destination blog/	#from the root of this repository
	```
 - To preview the blog locally:
 	``` 
	jekyll serve		#from the root of this repository
	```
	The output of jekyll serve should have at the bottom:
	```
	    Server address: http://127.0.0.1:4000/
	    Server running... press ctrl-c to stop.
	```
	Open [http://127.0.0.1:4000/](http://127.0.0.1:4000/) in your browser to preview the blogs
	
 - To test for errors:
	```
	htmlproofer ./_site --disable-external		#from the root of this repository
	```
	The final output of htmlproofer should be something like:
	```
	Ran on XYZ files!
	
	HTML-Proofer finished successfully.
	```
	If not, check for missing links and follow the error message
 - Remove the build files before making your commits
 	```
	rm -r blog/
	```
	
### Step 5: Pushing your article to the repository
- Create a new branch in your local repository and commit your changes to it.
- Push the newly created branch to the main repository and create a Pull Request
- When making the pull request follow this:
		- Title : New article: (post title)
		- Description : A short description about your article
		
Resolve merge conflcts in your Pull Request, if any. Refer to [this](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-on-github) link on resolving merge conflicts or try googling or ask someone on our Slack workspace under the #github channel.
