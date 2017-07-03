import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { RegistrationComponent } from './registration/registration.component';
import { SuccessComponent } from './success/success.component';


const routes: Routes = [
  { path: '', pathMatch: 'full', component:RegistrationComponent},
  { path: 'login', component:LoginComponent},
  { path: 'success', component:SuccessComponent }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
