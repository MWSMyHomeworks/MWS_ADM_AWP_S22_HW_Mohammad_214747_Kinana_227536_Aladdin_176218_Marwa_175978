from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# noinspection PyPackages
from .predictFunction import predictResult


class LoanStatusViews(APIView):
    # noinspection PyMethodMayBeStatic
    def post(self, request):
        # noinspection PyPep8Naming
        customersData = request.data['CustomersData']
        # noinspection PyPep8Naming
        customersDataArray = []
        for customerData in customersData:
            customersDataArray.append(
                [
                    customerData['Gender'],
                    customerData['Married'],
                    customerData['Dependents'],
                    customerData['Education'],
                    customerData['SelfEmployed'],
                    customerData['ApplicantIncome'],
                    customerData['CoApplicantIncome'],
                    customerData['LoanAmount'],
                    customerData['LoanAmountTerm'],
                    customerData['CreditHistory']
                ]
            )
        # noinspection PyPep8Naming
        modelFileName = request.data['Model']
        results = predictResult(customersDataArray, modelFileName)
        return Response(results, status=status.HTTP_200_OK)
