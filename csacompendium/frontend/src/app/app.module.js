import '../assets/css/main.css';
import '../test_users.html';
import '../test_index.html';
import angular from 'angular';
import appCore from './core/core.module';
import layoutCore from './layout/layout.module';

angular.module('app', [
    appCore.name,
    layoutCore.name
]);

import './layout/collapse-section.ctrl';
