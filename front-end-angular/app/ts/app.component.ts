import {Component} from 'angular2/core';
import {LoginComponent} from './login.component'

@Component({
    selector: 'my-app',
    template: "<login>Login Component didnt get called</login>",
    directives: [LoginComponent]
})
export class AppComponent { 
}