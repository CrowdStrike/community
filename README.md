# Welcome!
This is the code behind https://crowdstrike.github.io/community/

On that webpage, you can find content such as:
- [List of CrowdStrike's Open Source Projects](https://crowdstrike.github.io/community/)
- [Guidance for CrowdStrike Engineering](https://crowdstrike.github.io/community/open-source-policy/#engineering)
- [Guidance for All Other Departments/Orgs](https://crowdstrike.github.io/community/open-source-policy/#everyone-else)



## Developing the Site

1. Ensure ``bundler`` and `jekyll` and ``rake`` are installed locally:
```shell
gem install bundler jekyll rake
```
2. Install NPM dependencies. The webroot is the `docs` folder, so you must change into that directory:
```shell
cd docs/ && npm install
```

3. Start the development server locally. It will watch for chances you make, and reload (nearly) instantly:
```shell
bundle exec jekyll serve
```

The ``bundle exec jekyll serve`` command will generate output similar to the following. It will include the hostname and port of your local instance:
```shell
Configuration file: /Users/swells/Documents/src/github/CrowdStrike/community/docs/_config.yml
            Source: /Users/swells/Documents/src/github/CrowdStrike/community/docs
       Destination: /Users/swells/Documents/src/github/CrowdStrike/community/docs/_site
 Incremental build: disabled. Enable with --incremental
      Generating... 
                    done in 4.785 seconds.
 Auto-regeneration: enabled for '/Users/swells/Documents/src/github/CrowdStrike/community/docs'
    Server address: http://127.0.0.1:4000
  Server running... press ctrl-c to stop.
```

