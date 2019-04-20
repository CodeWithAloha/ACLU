# Code for Hawaii + ACLU
# Access to public lands in Hawai`i App
Welcome!  [Code for Hawaii](http://www.codeforhawaii.org) has partnered with the [American Civil Liberties Union of Hawai`i](https://acluhi.org) ("ACLU") to create an app.  The intent of the proposed app is to use your geo-location to assist understanding of whose land you are on and your civil rights there.

Please start by reading the [project proposal](docs/ACLU-Access-App.pdf).

*Questions? Want to help?*  
**Come join us** on Wednesday nights at the [Code for Hawaii meetups](https://www.meetup.com/Code-for-Hawaii/).  We meet the first three Wednesdays of the month.  (Contact Ryan for Saturday morning hack sessions too). 

**Quick Links**
* [General project board](https://github.com/CodeforHawaii/ACLU/projects/4)
* [Data sources spreadsheet](https://docs.google.com/spreadsheets/d/1eDXV0qamY_5pcfe0SZbqs2PQXR_yJUs0-liX7sJo3wE/)
* [App Prototype](https://invis.io/P8NLK5NZ2YU)

## Frontend Development

We are using Vue.js for our frontend. The project was created using [vue-cli](https://cli.vuejs.org/).
If you look at the folder structure you will see a `frontend` and a `frontend` folders. Go for the `v2` :)

Updated dev instructions (using nvm):
1. Install nvm using `curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash`
1. Install node: `nvm install node`
1. Use nvm install node: `nvm use node`
1. Install vue.js and friends:`npm install -g @vue/cli; npm install -g @vue/cli-service-global; npm install babel-plugin-transform-runtime`

To run the vue and view the site:
1. Use node frm nvm: `nvm use node; npm run serve`
1. Go to [http://localhost:8080/](http://localhost:8080/) in your browser


Other useful commands:
1. To audit packages: `nvm use node; npm audit`
1. To lint the code:  `nvm use node; npm lint`
1. To run tests: `nvm use node; npm run test`


Old instructions (using npm):

1. `cd frontend`
1. `npm install`
1. `npm run serve`
1. Open http://localhost:8080




## Backend Development

Sorry, we are not doing much work on the backend these days and the steps to setup a dev environment for the database are kind of cumbersome. If you are interested in helping on our backend, feel free to drop by our Wednesday meetup and we can happily walk you through the process.
Just as a heads ups, we are using MongoDB + Python/Flask + Eve.
