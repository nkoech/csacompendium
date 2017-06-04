require('../assets/css/main.css');
require('angular');
require('./core/core.module');
require('./layout/layout.module');
require('./home/home.module');

angular.module('app', [
    'app.core',
    'app.layout',
    'app.home'
]);