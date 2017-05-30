require('../assets/css/main.css');
require('../test_users.html');
require('../test_index.html');
require('angular');
require('./core/core.module');
require('./layout/layout.module');

angular.module('app', [
    'app.core',
    'app.layout'
]);