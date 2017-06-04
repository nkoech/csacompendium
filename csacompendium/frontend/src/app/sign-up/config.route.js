angular
    .module('app.sign-up')
    .config(routes);

function routes($routeProvider, $locationProvider) {
    $routeProvider.
        when('/sign-up', {
            title: 'sign-up',
            controller: 'SignUpController',
            controllerAs: 'vm',
            templateUrl: require("./sign-up.tpl.html")
        });
    $locationProvider.html5Mode(true);
}