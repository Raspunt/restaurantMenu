from django.shortcuts import render

from . models import Category,Product


def MainPage(request):
    category = Category.objects.all()
    return render(request,'restoran/index.html',
    {
        'category':category
    })


def CategoryDetail(request,category_id):

    category = Category.objects.get(id=category_id)
    products = category.products.all()


    return render(request,'restoran/CategoryMenu.html',
    {
        'category':category,
        'products':products
    })



def CategoryCreate(request):
    
    if request.method == "POST":

        title = request.POST['title']
        file = request.FILES['file']  

        Category.objects.create(title=title,image=file)





    return render(request,"restoran/CategoryCreate.html")


def ProductCreate(request):

    print(request.FILES)
    if request.method == "POST":

        title = request.POST['title']
        image = request.FILES['file']  
        price = request.POST['price']
        price_valuta = request.POST['price_valuta']
        CategoryId = request.POST['CategoryId']

        product = Product.objects.create(
                        title=title,
                        image=image,
                        price=price,
                        price_valuta=price_valuta,
                    )
        category = Category.objects.get(id=CategoryId)

        category.products.add(product)


        


    return render(request,"restoran/ProductCreate.html")



