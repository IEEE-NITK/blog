import os
import shutil
import sys

def process_image_line(lineNumber, blogFileName, line):
    # Get the image name
    imageName = line.split('[')[1].split(']')[0].strip()

    # Get the image path
    imagePath = line.split('(')[1].split(')')[0].strip()

    # Get the image extension
    imageExtension = imagePath.split('.')[-1]

    # Create the new image name
    newImageName = blogFileName.split('.')[0] + '-' + imageName + '.' + imageExtension

    # Create the new image path
    newImagePath = imagePath.replace(imageName, newImageName)

    # Replace the image path in the line
    line = line.replace(imagePath, newImagePath)

    # Transfer the image to the new image path
    shutil.copy(f'images/{imageName}', newImagePath)

    return line

def writeUserInfo(githubUsername):
    name = input('Enter ', githubUsername, ' name: ')
    email = input('Enter ', githubUsername, ' email: ')
    author_image = input('Enter ', githubUsername, ' image name (This is the name of the profile picture of the image of the author THAT MUST BE IN THE images/ folder in THIS CURRENT DIRECTORY) : ')
    with open('auther_info.txt', 'a') as f:
        f.write(githubUsername: + '\n')
        f.write("  name: " + name + '\n')
        f.write("  github: " + githubUsername + '\n')
        f.write("  author_image: " + author_image + '\n')
        f.write("  email: " + email + '\n')
    

def parse(markdownBlog):
    with open(markdownBlog, 'r') as f:
        githubUsername1 = ['', 0]
        githubUsername2 = ['', 0]
        blogTitle = ''
        blogDate = ''
        blogFileName = ''
        for (i, line) in enumerate(f):
            if line.startswith('title:'):
                blogTitle = line.split(':')[1].strip()
            if line.startswith('date:'):
                blogDate = line.split(':')[1].strip()
            if line.startswith('github_username_1:'):
                githubUsername1[0] = line.split(':')[1].strip()
                githubUsername1[1] = i
            if line.startswith('github_username_2:'):
                githubUsername2[0] = line.split(':')[1].strip()
                githubUsername2[1] = i
            if '![' in line:
                blogFileName = blogDate + '-' + blogTitle.replace(' ', '-') + '.md'
                newline = process_image_line(i, blogFileName, line)
                line = newline
        
    # Go to the github_username_1 line and change github_username_1 to the github_username
    lines = open(markdownBlog, 'r').readlines()
    lines[githubUsername1[1]] = 'github_username: ' + githubUsername1[0] + '\n'

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

    open(blogFileName, 'w').writelines(lines)
    
    finalSteps(blogFileName, markdownBlog)

def finalSteps(blogFileName, markdownBlog):
    # Move the blog to the _posts folder
    shutil.move(blogFileName, '_posts/' + blogFileName)

    # Delete the markdown blog
    os.remove(markdownBlog)

    # Delete the images folder
    shutil.rmtree('images')

    # append auther_info.txt to _data/auther_info.yml
    with open('auther_info.txt', 'r') as f:
        lines = f.readlines()
        with open('_data/auther_info.yml', 'a') as f2:
            f2.writelines(lines)
    os.remove('auther_info.txt')


if __name__ == '__main__':
    markdownBlog = sys.argv[1]
    parse(markdownBlog)