---
title: Contributing
description: This is a documentation page.
permalink: /contributing/

layout: post
sidenav: contributing
subnav:
  - text: Welcome
    href: '#contributing-welcome'
  - text: Using Git
    href: '#contributing-git'
---

## Welcome to the CrowdStrike Community

Hello and welcome to the CrowdStike community on GitHub! Any and all contributions are welcome. The community may not always merge or act on something, but that is okay!
Please keep engaging us.

Speaking of engaging the community, there are a couple of things to consider:

1. If you have general questions of the community that are not around specific repositories or projects, please [open a community discussion](https://github.com/CrowdStrike/community/discussions/new).
1. If you do not see a project, repository, or would like us to consider working on a specific piece of technology, please [open a community ticket](https://github.com/CrowdStrike/community/issues/new). These type of requests should not be made in existing projects.
1. If there is a specific issue or enhancement you would like to see addressed in a particular project, please open an issue in that project. It might be tempting to open a discussion, but an issue is more appropriate to address the problem.
1. If you have general questions of a project, please open a discussion in that project instead of a community discussion.

Thank you and happy coding!

## Using Git

### Forking Projects

When contributing to projects, 

1. Please fork the CrowdStrike project to your GitHub Account. [Example on how to fork a repository](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#fork-an-example-repository)
1. Once the project is forked to your own account, clone the project to your local system. [Example on cloning a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#about-cloning-a-repository)
1. Change directory to the repository folder, and create a new branch by running `git checkout -b my_change` where `my_change` is a short drescription of the change being made. Changes should be made in the new branch vs the `main` branch because you normally want your `main` branch to match with the original CrowdStrike repository `main` branch.
1. Make the desired changes in the repository.
1. Push the branch back to your GitHub account. For example, `git push origin my_change` where `my_change` is name of the branch.
1. Create a pull request in the original CrowdStrike project that you forked. [Example on how to create a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork)

### Rebasing

You should rarely develop or make changes to your local `main` branch, but sometimes, your `main` branch gets out of date. Also, some pull requests may have been merged that might require
that the branch on which you are developing contains the latest commits.

1. Make sure your `main` branch is up-to-date from the CrowdStrike repository before creating new branches. [Example on syncing a fork](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)
1. Once your `main` branch has been synced, rebase your working branch (before you create a pull request) by checking out your branch and then running `git rebase -i main`.
2. For handling merge conflicts, see [how to resolve a git merge conflict](https://opensource.com/article/20/4/git-merge-conflict) for a walkthrough on handling merge conflicts.

#### Squashing

Before submitting pull requests, please make sure to squash commits in your branch when:

1. You create multiple commits (use `git log` to show history) that have the same commit message like `Update Readme.md`.
1. Created a bunch of junk or throw away commit messages like `Fix`, `Test`, `Fixed Typos`, etc.

[Example on squashing commits using git rebase](https://garrytrinder.github.io/2020/03/squashing-commits-using-interactive-rebase)
