class UserStatus:
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    BANNED = 'banned'

    CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (BANNED, 'Banned'),
    ]


class UserGender:
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]


class SocialProvider:
    FACEBOOK = 'facebook'
    GOOGLE = 'google'
    TWITTER = 'twitter'

    CHOICES = [
        (FACEBOOK, 'Facebook'),
        (GOOGLE, 'Google'),
        (TWITTER, 'Twitter'),
    ]


class TourFeatured:
    HOT = 'hot'
    NEW = 'new'
    NORMAL = 'normal'

    CHOICES = [
        (HOT, 'Hot'),
        (NEW, 'New'),
        (NORMAL, 'Normal'),
    ]


class TourTripStatus:
    BOOKING = 'booking'
    ONGOING = 'ongoing'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

    CHOICES = [
        (BOOKING, 'Booking'),
        (ONGOING, 'Ongoing'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    ]


class BookingStatus:
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
    REFUNDED = 'refunded'

    CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
        (REFUNDED, 'Refunded'),
    ]


class TourGuideStatus:
    ACTIVE = 'active'
    INACTIVE = 'inactive'

    CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]


class PaymentMethod:
    INTERNET_BANKING = 'internet_banking'
    CREDIT_CARD = 'credit_card'
    CASH = 'cash'

    CHOICES = [
        (INTERNET_BANKING, 'Internet Banking'),
        (CREDIT_CARD, 'Credit Card'),
        (CASH, 'Cash'),
    ]


class PaymentStatus:
    PENDING = 'pending'
    COMPLETED = 'completed'
    FAILED = 'failed'
    REFUNDED = 'refunded'

    CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed'),
        (REFUNDED, 'Refunded'),
    ]
