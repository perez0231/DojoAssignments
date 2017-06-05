class TimesController < ApplicationController
  def index
    @time = Time.now.strftime("%d/%m/%Y %H:%M")

  end
end
