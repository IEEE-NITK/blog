import os
import shutil
import sys

YEAR = '2023'

def process_image_line(lineNumber, blogFileName, line):
    # Get the image path
    imagePath = line.split('(')[1].split(')')[0].strip()

    # Get the image name
    imageName = imagePath.split('/')[-1]

    # Get the image extension
    imageExtension = imagePath.split('.')[-1]

    # Create the new image name
    newImageName = blogFileName.split('.')[0] + '-' + imageName

    # Create the new image path
    newImageFolderPath = '../assets/img/' + blogFileName.split('.')[0] + '/'
    forMarkdownImagePath = '/blog/assets/img/' + blogFileName.split('.')[0] + '/' + newImageName
    newImagePath = newImageFolderPath + newImageName

    # Replace the image path in the line
    line = line.replace(imagePath, forMarkdownImagePath)

    # Transfer the image to the new image path
    if not os.path.exists(newImageFolderPath):
        os.makedirs(newImageFolderPath)
    shutil.copy(f'images/{imageName}', newImagePath)

    return line


def writeUserInfo(githubUsername):
    name = input('Enter ' + githubUsername + ' name: ')
    email = input('Enter ' + githubUsername + ' email: ')
    author_image = input('Enter '+ githubUsername + ' image name (This is the name of the profile picture of the image of the author with extension THAT MUST BE IN THE images/ folder in THIS CURRENT DIRECTORY) : ')
    imageName = YEAR + name.replace(' ', '-') + '.jpg'
    with open('author_info.txt', 'a', encoding='utf-8') as f:
        f.write(githubUsername + ':\n')
        f.write("  name: " + name + '\n')
        f.write("  github: " + githubUsername + '\n')
        
        if author_image == '':
            author_image = 'blog-author.jpg'
        
        f.write("  author_image: " + imageName + '\n')
        f.write("  email: " + email + '\n')
    # copy the author image to the images folder
    shutil.copy('images/'+author_image, '../assets/img/authors/' + imageName)
    

def parse(markdownBlog):
    print('Parsing: ' + markdownBlog)
    lines = open(markdownBlog, 'r',  encoding='utf-8').readlines()
    with open(markdownBlog, 'r') as f:
        githubUsername1 = ['', 0]
        githubUsername2 = ['', 0]
        blogTitle = ''
        blogDate = ''
        blogFileName = ''
        for (i, line) in enumerate(lines):
            if line.startswith('title:'):
                blogTitle = line.split(':')[1].strip()
            if line.startswith('date:'):
                blogDate = line.split(':')[1].strip()
                blogDate = blogDate.split(' ')[0]
            if line.startswith('github_username_1:'):
                githubUsername1[0] = line.split(':')[1].strip()
                githubUsername1[1] = i
                # remove double and single quotes from the githubUsername1 if it has any
                githubUsername1[0] = githubUsername1[0].replace('"', '')
                githubUsername1[0] = githubUsername1[0].replace("'", '')
                githubUsername1[0] = githubUsername1[0].replace("”", '')
                githubUsername1[0] = githubUsername1[0].replace("“", '')


            if line.startswith('github_username_2:'):
                githubUsername2[0] = line.split(':')[1].strip()
                githubUsername2[1] = i
                # remove double and single quotes from the githubUsername2 if it has any
                githubUsername2[0] = githubUsername2[0].replace('"', '')
                githubUsername2[0] = githubUsername2[0].replace("'", '')
                githubUsername2[0] = githubUsername2[0].replace("”", '')
                githubUsername2[0] = githubUsername2[0].replace("“", '')

            if '![' in line:
                blogFileName = blogDate + '-' + blogTitle.replace(' ', '-') + '.md'
                # remove quotes from the blogFileName
                blogFileName = blogFileName.replace('"', '')
                newline = process_image_line(i, blogFileName, line)
                lines[i] = newline
        
    # Go to the github_username_1 line and change github_username_1 to the github_username
    
    # remove quotes from the githubUsername1
    githubUsername1[0] = githubUsername1[0].replace('"', '')
    githubUsername1[0] = githubUsername1[0].replace("'", '')

    # remove quotes from the githubUsername2
    githubUsername2[0] = githubUsername2[0].replace('"', '')
    githubUsername2[0] = githubUsername2[0].replace("'", '')

    lines[githubUsername1[1]] = 'github_username: ' + githubUsername1[0] + '\n'
    lines[githubUsername2[1]] = 'github_username_2: ' + githubUsername2[0] + '\n'

    if githubUsername2[0] != '':
        print('2 Author Blog')
        print('Author 1: ' + githubUsername1[0])
        writeUserInfo(githubUsername1[0])
        print('Author 2: ' + githubUsername2[0])
        writeUserInfo(githubUsername2[0])
    else :
        print('1 Author Blog')
        print('Author 1: ' + githubUsername1[0])
        writeUserInfo(githubUsername1[0])

    
    # Write the lines back to the file 

    open(blogFileName, 'w', encoding='utf-8').writelines(lines)
    
    finalSteps(blogFileName, markdownBlog)


def finalSteps(blogFileName, markdownBlog):
    # Move the blog to the _posts folder
    
    shutil.move(blogFileName, '../_posts/' + blogFileName)

    # Delete the markdown blog
    os.remove(markdownBlog)

    # Delete the images folder
    shutil.rmtree('images')

    # append author_info.txt to _data/author_info.yml
    with open('author_info.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        with open('../_data/authors.yml', 'a', encoding='utf-8') as f2:
            f2.write('\n')
            f2.writelines(lines)
    os.remove('author_info.txt')


if __name__ == '__main__':
    markdownBlog = sys.argv[1]
    parse(markdownBlog)