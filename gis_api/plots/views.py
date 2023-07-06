from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer, PlotSerializer
from .models import Plot


class LoginView(APIView):
    """
    Get the current user or Login a user.
    """
    def get(self, request):
        """
        Get the current user.
        args: a request object
        return: Response object containing user data
        """
        serializer = UserSerializer(request.user)
        return Response({'current_user': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Try to authenticate a user.
        args: a request object
        return: Response object containing user data if successfull
        """
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            serializer = UserSerializer(request.user)
            return Response({'current_user': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    """
    Logout the current user.
    """
    def get(self, request):
        """
        Logout the current user.
        args: a request object
        return: Response object containing user data
        """
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)


class MyPlotsView(APIView):
    """
    As a user : List or Add plots.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        List user plots.
        args: a request object
        return: Response object containing user plots
        """
        plots = Plot.objects.filter(user=request.user)
        serializer = PlotSerializer(plots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        Create user plot.
        args: a request object
        return: Response object containing the new user plot
        """
        serializer = PlotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ManagePlotView(APIView):
    """
    Managing (Get, Delete or Update) user plots.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """
        Get a specific user plot.
        args: 
            a request object, 
            pk(int):plot id
        return: Response object containing plot data
        """
        try:
            plot = Plot.objects.get(pk=pk, user=request.user)
        except Plot.DoesNotExist:
            return Response({'message': 'Plot not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlotSerializer(plot)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
    
    def patch(self, request, pk):
        """
        Update a specific user plot.
        args:
            a request object, 
            pk(int):plot id
        return: Response object containing plot data
        """
        try:
            plot = Plot.objects.get(pk=pk, user=request.user)
        except Plot.DoesNotExist:
            return Response({'message': 'Plot not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlotSerializer(plot, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message': 'malformed data'}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        """
        Delete a specific user plot.
        args:
            a request object, 
            pk(int):plot id
        return: Response object
        """
        try:
            plot = Plot.objects.get(pk=pk, user=request.user)
        except Plot.DoesNotExist:
            return Response({'message': 'Plot not found'}, status=status.HTTP_404_NOT_FOUND)

        plot.delete()
        return Response({'message': 'Plot deleted'}, status=status.HTTP_200_OK)