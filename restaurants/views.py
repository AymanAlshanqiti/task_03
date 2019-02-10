from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list": [
    		{
    			"restaurant_name": "Hashi",
    			"food_type": "Arabic Food",
    		},
    		{
    			"restaurant_name": "Byato",
    			"food_type": "Italian Food",
    		},
    		{
    			"restaurant_name": "Makani",
    			"food_type": "Indian Food",
    		},
    	
    	],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object": 
    		{
    			"restaurant_name": "Byato",
    			"food_type": "Italian Food",
    		},

    }
    return render(request, 'detail.html', context)
