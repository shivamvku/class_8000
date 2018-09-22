# Devtools
	
# 	1.pip 
# 	2.virtualenv
# 	3.git

# ========================
# pip
# =======================

# it is a packge manger it perofrms the fowlling opertions

#   install                     Install packages.
#   download                    Download packages.
#   uninstall                   Uninstall packages.
#   freeze                      Output installed packages in requirements format.
#   list                        List installed packages.
#   show                        Show information about installed packages.
#   check                       Verify installed packages have compatible dependencies.
#   config                      Manage local and global configuration.
#   search                      Search PyPI for packages.
#   wheel                       Build wheels from your requirements.
#   hash                        Compute hashes of package archives.
#   completion                  A helper command used for command completion.




#  pip -------------- PyPI (python.org)


# PyPI ------ python package index

# pip3 installe pkgname

# ====================================================
# # virtual Enviromet
# ===================================================



# virtualenv ------- It is a python package and  It is used to create isolated python Projects

# p1
# numpyy 1.0

# p2 
# numpyy 2.0

# p3

# numpyy 5.6




# Installation if virtualenv
# -------------------------
# pip3 install virtualenv


# # Creaating a Project of Python and Enviromet
# # ==============================================


# virtualenv Dummyprj


# Activation
# -----------------------
# ==========
# IN LINUX 
# =========
# 	cd Projectfolder
# 		cd bin
# 			source ./activate
# ==========
# IN WINDOWS
# ===========
# 	cd Projectfolder
# 		cd Scripts
# 			activate



# Deactivate
# ------------------------------

# Type just Deactivate





# ==========================
# GIT HUB
# ========================

# GitHub is a development platform to  host and 
# review code, manage projects,
# and build software alongside 


# Git is a free and open source distributed 
# version control system designed 
# to handle everything from small to very large
# projects with speed and efficiency.



# Stepts
# =============

# accout Creaating
# -------------------------

# create account in https://github.com


# ===============
# Download git
# ================

# 		# ==========
# 		# IN WINDOWS
# 		# ===========
# 			1.go to https://git-scm.com/
# 			2.Download for WINDOWS
# 		# ============
# 		# IN LINUX
# 		# ============
# 			sudo apt-get install git

# =================================
# GIt configuration and setup CONFIGURE TOOLING
# ==================================+

=======================================================
Configure user information for all local repositories
========================================================

1.Sets the name you want atached to your commit transactions
	-----$ git config --global user.name "[name]"

2.Sets the email you want atached to your commit transactions

	-----$ git config --global user.email "[email address]"


==========================================================
CREATE REPOSITORIES
============================================================
1.Start a new repository or obtain one from an existing URL
		$ git init [project-name]
2.Creates a new local repository with the specified name
		$ git clone [url]
	Downloads a project and its entire version history


=========================================================
MAKE CHANGES
====================================================
1.Lists all new or modified files to be commited

	$ git status
2.Snapshots the file in preparation for versioning

	$ git add [file]

3.Records file snapshots permanently in version history
	$ git commit -m "[descriptive message]"

=============================================
SYNCHRONIZE CHANGES
==============================================
1.Uploads all local branch commits to GitHub
	$ git push [alias] [branch]
2.Downloads bookmark history and incorporates changes
	$ git pull