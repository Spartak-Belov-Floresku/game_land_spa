import { Container } from 'react-bootstrap'
import { 
  BrowserRouter as Router, 
  Routes, 
  Route, 
  Navigate 
} from 'react-router-dom'

import Header from './components/Header'
import Footer from './components/Footer'

import HomeScreen from './screens/HomeScreen'
import ProductScreen from './screens/ProductScreen'
import CartScreen from './screens/CartScreen'
import LoginScreen from './screens/LoginScreen'
import RegisterScreen from './screens/RegisterScreen'
import ProfileScreen from './screens/ProfileScreen'
import ShippingScreen from './screens/ShippingScreen'
import PaymentScreen from './screens/PaymentScreen'
import PlaceorderScreen from './screens/PlaceorderScreen'
import OrderScreen from './screens/OrderScreen'
import UserListSreen from './screens/UserListSreen'

function App() {
  return (
    <Router>
      <Header/>
        <main className='py-3'>
          <Container>
            <Routes>
              <Route path='/' element={<HomeScreen />} />
              <Route exact path='/login' element={<LoginScreen />} />
              <Route path='/login/:redirect' element={<LoginScreen />} />
              <Route exact path='/register' element={<RegisterScreen />} />
              <Route path='/register/:redirect' element={<RegisterScreen />} />
              <Route path='/profile' element={<ProfileScreen />} />
              <Route path='/product/:productId' element={<ProductScreen />} />
              <Route exact path='/cart' element={<CartScreen />} />
              <Route path='/cart/:productId/:qty' element={<CartScreen />} />
              <Route path='/shipping' element={<ShippingScreen />} />
              <Route path='/payment' element={<PaymentScreen />} />
              <Route path='/placeorder' element={<PlaceorderScreen />} />
              <Route path='/order/:orderId' element={<OrderScreen />} />

              <Route path='admin/userlist' element={<UserListSreen />} />

              <Route path="*" element={<Navigate to="/" replace />} />
            </Routes>
          </Container>
        </main>
      <Footer/>
    </Router>
  );
}

export default App;
