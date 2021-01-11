# remove doc/_build/html if present
rm -rf _build/html

#create a new directory (in doc/)
mkdir -p _build/html


# clone the entire repo into this directory (yes, this duplicates it)
git clone git@github.com:username/project.git _build/html

# set this directory to track gh-pages
git symbolic-ref HEAD refs/heads/gh-pages
rm .git/index
git clean -fdx

# _build/html, but not overwrite the .git directory
make html

# now, add these bad-boys to the gh-pages repo, along with .nojekyll:
cd _build/html
git add .
git commit -m 'deploy to gh-pages'
git pull origin master