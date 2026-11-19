class ProductFilterOptions:
    PRICE_LOW_TO_HIGH = "lohi"
    PRICE_HIGH_TO_LOW = "hilo"
    NAME_A_TO_Z = "az"
    NAME_Z_TO_A = "za"


class CheckoutFormInfo:
    FIRST_NAME = "John"
    LAST_NAME = "Doe"
    ZIP_CODE = "82718"


class CheckoutMessages:
    CHECKOUT_TITLE = "Thank you for your order!"
    CHECKOUT_TEXT = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"


class AuthenticationErrorMessages:
    ERROR_INVALID_CREDENTIALS = "Epic sadface: Username and password do not match any user in this service"
    ERROR_USERNAME_REQUIRED = "Epic sadface: Username is required"
    ERROR_PASSWORD_REQUIRED = "Epic sadface: Password is required"
    ERROR_USER_LOCKED = "Epic sadface: Sorry, this user has been locked out."
    ERROR_ACCESSING_INVENTORY_NOT_LOGGED_IN = "Epic sadface: You can only access '/inventory.html' when you are logged in."


class CheckoutFormErrorMessages:
    ERROR_FIRST_NAME_REQUIRED = "Error: First Name is required"
    ERROR_LAST_NAME_REQUIRED = "Error: Last Name is required"
    ERROR_POSTAL_CODE_REQUIRED = "Error: Postal Code is required"
