import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { MyComponentComponent } from './my-component/my-component.component';
import { MainComponent } from './main/main.component';
import { HeaderComponent } from './header/header.component';
import { LeftComponent } from './main/left/left.component';
import { RightComponent } from './main/right/right.component';

@NgModule({
  declarations: [
    AppComponent,
    MyComponentComponent,
    MainComponent,
    HeaderComponent,
    LeftComponent,
    RightComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
