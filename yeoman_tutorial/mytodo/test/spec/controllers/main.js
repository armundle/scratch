'use strict';

describe('Controller: MainCtrl', function () {

  // load the controller's module
  beforeEach(module('mytodoApp'));

  var MainCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    MainCtrl = $controller('MainCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should have no items at start', function () {
    expect(scope.todos.length).toBe(0);
  });

  it('should add one item', function () {
    scope.todo = 'Test 1';
    scope.addTodo();
    expect(scope.todos.length).toBe(1);
  });

  it('should add one item and then remove it', function () {
    scope.todo = 'Test 1';
    scope.addTodo();
    scope.removeTodo(0);
    expect(scope.todos.length).toBe(0);
  });
});
