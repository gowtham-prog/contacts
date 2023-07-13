from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import User, Portfolio, Contact,Mapper
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from . serializers import contactserializer


@permission_classes((AllowAny,))
class register(APIView): #Registers the User
    def post(self, request):   #Create new User
        if request.data["name"] is None or request.data["mobile"] is None:  
            return Response({
                "ERROR" : "Please Enter The Details For Registration"
            },status= status.HTTP_400_BAD_REQUEST)
        try :
            if request.data["email"]:
                email = request.data["email"]
        except:
            email= "NONE"
        user = User(username = request.data["name"],password = request.data["password"], email = email)
        if user:
            user.set_password(request.data["password"])
            user.save()
            potfolio = Portfolio.objects.create(user=user, mobile= request.data["mobile"],email=email)
            return Response({
                "success": "User registered succesfully"
            }, status = status.HTTP_202_ACCEPTED)
        else:
            return Response({
                "ERROR" : "Encountered an error"
            },status = status.HTTP_400_BAD_REQUEST)
        

@permission_classes((AllowAny, ))                             
class login(APIView): #Login_view
    def post(self,request):
        if not request.data:
            return Response({
                "ERROR" : "Please provide a username and pasword"
            }, satus = status.HTTP_400_BAD_REQUEST)
        username = request.data.get("name")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({
                "ERROR" : "Bad Credentials"
            }, status = status.HTTP_400_BAD_REQUEST)
        user = authenticate(username = username,password = password)
        token,_ = Token.objects.get_or_create(user = user)
        return Response ({
            "token" : token.key
        }, status = status.HTTP_200_OK)
    

class contacts(APIView):  #retrieve and svae contacts
    def get (self,request):  #retrieve contacts                                                
        contact = Contact.objects.all()
        serializer = contactserializer(contact,many =True)
        return Response(serializer.data)
    def post(self,request):  #create new contact
        if request.data["name"] is None or request.data["mobile"] is None:
            return Response ({
                "ERROR" : "Name and Mobile are required Fields"
            },satus = status.HTTP_400_BAD_REQUEST)
        try :
            if request.data["email"]:
                email = request.data["email"]
        except:
            email= "NONE"  
        contact = Contact.objects.create(name = request.data["name"],mobile= request.data["mobile"],email = email)  
        mapper = Mapper.objects.create(user= request.user, contact= contact)
        return Response({
            "Success" : "contact Saved Succesfully"
        },status = status.HTTP_201_CREATED)
    


class Spam(APIView):   #can mark spam
    def post(self,request):    # update contact as spam
        mobile = request.data.get("mobile")
        if request.data["mobile"] is None:
            return Response({
                "ERROR": "You must provide the Mobile Number"
            },status = status.HTTP_400_BAD_REQUEST)
        contact = Contact.objects.filter(mobile = mobile).update(spam= True)
        portfolio = Portfolio.objects.filter(mobile = mobile).update(spam=True)
        if (contact+portfolio) :
            return Response({
                "Success" : "Marked as spam"
            }, status= status.HTTP_201_CREATED)
        else:
            return Response({
                "ERROR" : "Mobile Not Found!"
            },status= status.HTTP_404_NOT_FOUND)


class Name_search(APIView):     #retrieve contacts by name
    def post(self,request):      #prompts the user for input for name
        name = request.data.get("name")
        if request.data.get("name") is None:
            return Response({
                "ERROR":"Name field is Required"
            }, status= status.HTTP_400_BAD_REQUEST)
        portfolio_begin=Portfolio.objects.filter(user__username__startswith=name)
        portfolio_s=Portfolio.objects.filter(user__username__contains=name).exclude(user__username__startswith=name)
        contact_begin=Contact.objects.filter(name__startswith=name)
        contact_s=Contact.objects.filter(name__contains=name).exclude(name__startswith=name)
        response=[]
        for contact in portfolio_begin:
            response.append(
                    {
                        "name":contact.user.get_full_name(),
                        "mobile":contact.mobile,
                        "spam":contact.spam,
                    }
                )
        for contact in contact_begin:
            response.append(
                    {
                        "name":contact.name,
                        "mobile":contact.mobile,
                        "spam":contact.spam,
                    }
                )
        for contact in portfolio_s:
            response.append(
                    {
                        "user":contact.user.get_full_name(),
                        "mobile":contact.mobile,
                        "spam":contact.spam,
                    }
                )
        for contact in contact_s:
            response.append(
                    {
                        "user":contact.name,
                        "mobile":contact.mobile,
                        "spam":contact.spam,
                    }
                )
        return Response(
                response,
                status=status.HTTP_200_OK
            )  


class Mobile_search(APIView):    #retrieves contact by mobile number
    def post(self,request):     #prompt the user for input of mobile number
        mobile = request.data.get("mobile")
        if request.data.get("mobile") is None:
            return Response({
                "ERROR":"Mobile field is Required"
            },status = status.HTTP_404_NOT_FOUND)
        
        try :
            portfolio= Portfolio.objects.get(mobile=mobile)
            user =User.objects.get(id = portfolio.id, is_active= True)
            return Response(
                    {
                        "name":user.username,
                        "mobile":portfolio.mobile,
                        "spam":portfolio.spam,
                        "email":portfolio.email
                    }
                )
        except Portfolio.DoesNotExist:
            contact=Contact.objects.filter(mobile=mobile)
            serializer=contactserializer(contact,many=True)
            return Response(
                    serializer.data
                )