import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../pages/LandingPage.vue'
import RoomPage from '../pages/RoomPage.vue'
import BookingPage from '../pages/BookingPage.vue'
import RoomDetailsPage from '../pages/RoomDetailsPage.vue'
import LoginPage from '../pages/LoginPage.vue'
import RegisterPage from '../pages/RegisterPage.vue'
import Dashboard from '../pages/Dashboard.vue'
import Reservation from '../pages/Reservation.vue'
import GuestManagment from '../pages/GuestManagment.vue'
import RoomManagment from '../pages/RoomManagment.vue'
import ReportPage from '../pages/ReportPage.vue'
import ReservationDetails from '../pages/ReservationDetails.vue'
import ManagerDashboard from '../pages/ManagerDashboard.vue'
import UserTypeSelection from '../pages/UserTypeSelection.vue' // Add this
import StaffHomePage from '../pages/StaffHomePage.vue'
import RoomDetailStaff from '../pages/RoomDetailStaff.vue'
import UserManagment from '../pages/UserManagment.vue'
import CustomerReservation from '../pages/CustomerReservation.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: UserTypeSelection // Make this the landing page
  },
  {
    path: '/guest',
    name: 'GuestHomePage',
    component: LandingPage, // This should be your guest landing page
    meta: { layout: 'LandingLayout' }
  },
 {
  path: '/staff',
  component: StaffHomePage,
  meta: { layout: 'DefaultLayout' },
  children: [
    { path: '', name: 'Dashboard', component: Dashboard },
    { path: 'reservation', name: 'Reservation', component: Reservation },
    { path: 'reservation/:id', name: 'ReservationDetails', component: ReservationDetails },
    { path: 'guests', name: 'GuestManagement', component: GuestManagment },
    { path: 'rooms', name: 'RoomManagement', component: RoomManagment },
      {path:'rooms/:id', name:'RoomDetailsStaff', component:RoomDetailStaff},
    { path: 'report', name: 'Report', component: ReportPage },
    { path: 'manager/dashboard', name: 'ManagerDashboard', component: ManagerDashboard },
    { path: 'user', name: 'UserManagment', component: UserManagment },
  ]
}
 
,
  {
    path: '/rooms',
    name: 'Rooms',
    component: RoomPage,
    meta: { layout: 'LandingLayout' }
  },
  {
    path: '/rooms/:id',
    name: 'RoomDetail',
    component: RoomDetailsPage,
    props: true,
    meta: { layout: 'LandingLayout' }
  },
  {
    path: '/booking',
    name: 'Booking',
    component: BookingPage,
    meta: { layout: 'LandingLayout' }
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage,
    meta: { layout: 'AuthLayout' } // You might want a different layout for auth
  },
  {
    path: '/signup',
    name: 'Register',
    component: RegisterPage,
    meta: { layout: 'AuthLayout' }
  },
  {
    path:'/customer/reservation',
    name:'CustomerReservation',
    component:CustomerReservation,
    meta: { layout: 'LandingLayout' }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router