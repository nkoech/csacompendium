angular
    .module('app.home')
    .config(routes);

function routes($routeProvider) {
    $routeProvider.
        when('/', {
            title: 'home',
            controller: 'HomeController',
            controllerAs: 'vm',
            templateUrl: require("./home.tpl.html")
        });
}