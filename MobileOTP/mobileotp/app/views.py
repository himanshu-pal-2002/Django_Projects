from django.shortcuts import render, redirect
from django.contrib import messages
import firebase_admin
from firebase_admin import auth

# Views for sending OTP:

def send_otp(request):
    if request.method == 'POST':
        mobile_number = request.POST.get('mobile_number')

        try:
            # Send OTP to the user's phone number
            user = auth.create_user(phone_number=mobile_number)
            messages.success(request, f'OTP sent to {mobile_number}.')
            request.session['verification_id'] = user.uid
            return redirect('verify_otp')
        except Exception as e:
            messages.error(request, f'Failed to send OTP: {str(e)}')

    return render(request, 'send_otp.html')

# Views for verifying OTP:


def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        verification_id = request.session.get('verification_id')

        try:
            # Verify the entered OTP
            auth.update_user(verification_id, phone_number=otp)
            messages.success(request, 'OTP verified successfully.')
        except Exception as e:
            messages.error(request, f'Failed to verify OTP: {str(e)}')

    return render(request, 'verify_otp.html')




