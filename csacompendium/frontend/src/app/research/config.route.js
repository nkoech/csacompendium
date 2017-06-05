angular
    .module('app.research')
    .config(routes);

function routes($routeProvider, $locationProvider) {
    $routeProvider.
        when('/research/:id', {
            title: 'research',
            controller: 'ResearchController',
            controllerAs: 'vm',
            templateUrl: require("./research.tpl.html")
        });
    $locationProvider.html5Mode(true);
}