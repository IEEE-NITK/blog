---
layout: post
title: "Test Article 2"
author_github: adharshkamath
date: 2020-04-20 10:10:44
image: '/assets/img/'
description: 'Getting familiar with Git core concepts and Git remotes'
tags:
- Github
categories:
- Compsoc
github_username: 'adharshkamath'
comments: true
---
Git is a distributed version control system. It means Git helps you manage different versions of your work, record the changes and helps different collaborators work parallelly on the same project.

Imagine that you are working on a big project involving many files and folders in it. You make a series of changes to your project and now finally when you compile it, you see the application is crashing or not working as expected. In such a case, Git is the best tool you could use. If you have recorded all your changes uniformly in Git, you can any time refer to those versions. Alternately, you can create a copy of your work at the beginning itself, and start working over it and if the changes work out correctly, you can try to merge them with your original project.

This blog mainly covers the following content:
1. [Git Core](#gitcore)
    - [The three Logical Areas](#logicalareas)
    - [Learning core commands in Git using example](#example)
2. [Git Branching and Merging](#gitbranchingandmerging)
    - [Branching](#branching)
    - [Git Stash](#stash)
    - [Merging](#merging)
    - [Merge Conflicts](#mergeconflicts)
    - [Detached HEAD](#detachedhead)
3. [Git Remotes](#gitremotes)
    - [GitHub](#github)
    - [Learning basic git remote commands](#remote)
    - [Working with two remotes](#tworemotes)

<a name="gitcore"></a>

Git Core:
------------

<a name="logicalareas"></a>

In a Git repository/folder, we have three three logical areas, namely:
- Working Tree
- Staging Area
- Commmit History
![Three Logical Areas](/blog/assets/img/A-Dive-into-Git_Directory/three_areas_git.png)

For more clarity on commit, consider taking snapshots of your staged changes.

Resources: 
------------

1. [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2)
2. [https://github.com/PointCloudLibrary/pcl/wiki/A-step-by-step-guide-on-preparing-and-submitting-a-pull-request](https://github.com/PointCloudLibrary/pcl/wiki/A-step-by-step-guide-on-preparing-and-submitting-a-pull-request)
3. [https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase)
4. [https://www.atlassian.com/git/tutorials/rewriting-history](https://www.atlassian.com/git/tutorials/rewriting-history)
5. [https://www.perforce.com/blog/vcs/how-use-git-hooks](https://www.perforce.com/blog/vcs/how-use-git-hooks)
6. [https://spin.atomicobject.com/2016/06/26/parallelize-development-git-worktrees/](https://spin.atomicobject.com/2016/06/26/parallelize-development-git-worktrees/)
