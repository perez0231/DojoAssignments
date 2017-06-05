class ProductsController < ApplicationController
  def index
    @products = Product.all
  end



def create
  Product.create(name: params[:name], description: params[:description])
  redirect_to '/products'
end

def new

end

def show
@product=Product.find(params[:id])
end
def total
  @products_count=Product.count
  render 'products/total'
end

def edit
  @product= Product.find(params[:id])
end

def update
  Product.find(params[:id]).update( name: params[:name], description: params[:description])
  redirect_to '/products'
end
def destroy
  Product.find(params[:id]).delete
  redirect_to '/products'
end
end
