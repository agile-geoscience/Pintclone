var app = angular.module("app",[]);

app.controller("AppCtrl", function ($http){
    var app = this;

    $http.get("api/pin").success(function(data){
        app.pins = data.objects;
    })

})