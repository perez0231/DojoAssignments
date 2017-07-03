import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {FormsModule} from '@angular/forms'
import { HttpModule } from '@angular/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { AppointmentService} from './appointment.service';
import { AppointmentsComponent } from './appointments/appointments.component';
import { MakeAppComponent } from './make-app/make-app.component';
import { DeleteComponent } from './delete/delete.component'

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    AppointmentsComponent,
    MakeAppComponent,
    DeleteComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpModule,
    FormsModule,
  ],
  providers: [AppointmentService],
  bootstrap: [AppComponent]
})
export class AppModule { }
