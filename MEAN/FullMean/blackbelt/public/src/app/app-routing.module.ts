import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { AppointmentsComponent } from './appointments/appointments.component'
import { MakeAppComponent } from './make-app/make-app.component'
import { DeleteComponent } from './delete/delete.component'


const routes: Routes = [
  { path: '', pathMatch: 'full', component: LoginComponent },
  { path: "appointments", component: AppointmentsComponent},
  { path: "makeAppointment", component: MakeAppComponent},
  { path: "delete/:id", component: DeleteComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
