require('../assets/css/main.css');
require('angular');
require('./core/core.module');
require('./layout/layout.module');
require('./home/home.module');
require('./about/about.module');
require('./case-studies/case-studies.module');
require('./login/login.module');
require('./sign-up/sign-up.module');


angular.module('app', [
    'app.core',
    'app.layout',
    'app.home',
    'app.about',
    'app.case-studies',
    'app.login',
    'app.sign-up'
]);