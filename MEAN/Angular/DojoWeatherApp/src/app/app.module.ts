import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpModule} from '@angular/http';
import { HttpService } from './http.service';
import { AppRoutingModule } from './app-routing.module';
//components
import { AppComponent } from './app.component';
import { SeattleComponent } from './seattle/seattle.component';
import { SanJoseComponent } from './san-jose/san-jose.component';
import { BurbankComponent } from './burbank/burbank.component';
import { DallasComponent } from './dallas/dallas.component';
import { ChicagoComponent } from './chicago/chicago.component';
import { DCComponent } from './dc/dc.component';

@NgModule({
  declarations: [
    AppComponent,
    SeattleComponent,
    SanJoseComponent,
    BurbankComponent,
    DallasComponent,
    ChicagoComponent,
    DCComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpModule,
  ],
  providers: [HttpService],
  bootstrap: [AppComponent]
})
export class AppModule { }
