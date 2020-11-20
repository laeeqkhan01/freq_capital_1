from django.shortcuts import render
from django.http      import HttpResponse

# Create your views here.

# Start Frequency MHz for a capital.
capitals = [
    "DC",
    "LONDON",
    "TOKYO",
    "PARIS",
]

def isFloat(dataString):
    try:
        float(dataString)
        return True   # can be converted to float
    except ValueError:
        return False  # Cant be converted to float

def checkFrequencyData(cap, startFrqStr, stopFrqStr):
    startFreqMHz = 0
    stopFreqMHz  = 0
    maxFreqMHz   = 6000

    if not(cap in capitals):
        retVal = "Dont have info about capital " + cap
        return retVal

    if isFloat(startFrqStr):
        startFreqMHz = float(startFrqStr)
        if startFreqMHz < 0:
            return "Start Frequency cannot be negative"
        if startFreqMHz > maxFreqMHz:
            retVal = "Start Frequency cannot be more than " + str(maxFreqMHz)
            return retVal
    else:
        return "Start frequency should be numeric"

    if isFloat(stopFrqStr):
        stopFreqMHz = float(stopFrqStr)
        if stopFreqMHz < startFreqMHz:
            return "Stop frequency cannot be less than start frequency"
        if stopFreqMHz > maxFreqMHz:
            retVal = "Stop Frequency cannot be more than " + str(maxFreqMHz)
            return retVal
    else:
        return "Stop frequency should be numeric"

    return "Everything is alright"

def homePageView(request):
    return render(request, 'freq_verification/homePageView.html')

def verifyfreq(request):
    postData = {}
    startFreqStr = request.POST.get("startfreq")
    stopFreqStr  = request.POST.get("stopfreq")
    capital      = request.POST.get("capital")

    retVal = checkFrequencyData(capital, startFreqStr, stopFreqStr)
    context = {'retVal': retVal}
    #return HttpResponse(retVal)
    return render(request, 'freq_verification/verification_result.html', context)
