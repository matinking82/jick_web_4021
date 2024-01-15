import { useState } from 'react'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <svg xmlns="http://www.w3.org/2000/svg" width="73" height="71" viewBox="0 0 73 71" fill="none">
        <g filter="url(#filter0_d_30_362)">
          <path d="M53 10.9H20C16.6863 10.9 14 13.3848 14 16.45V46.975C14 50.0402 16.6863 52.525 20 52.525H53C56.3137 52.525 59 50.0402 59 46.975V16.45C59 13.3848 56.3137 10.9 53 10.9Z" fill="#4482BA" />
        </g>
        <path d="M32 35.875L28 32.175L32 35.875ZM28 32.175L32 28.475L28 32.175ZM28 32.175H46H28Z" fill="#4482BA" />
        <path d="M28 32.175H46M32 35.875L28 32.175L32 35.875ZM28 32.175L32 28.475L28 32.175Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        <defs>
          <filter id="filter0_d_30_362" x="0" y="0.900024" width="73" height="69.625" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
            <feFlood flood-opacity="0" result="BackgroundImageFix" />
            <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha" />
            <feOffset dy="4" />
            <feGaussianBlur stdDeviation="7" />
            <feColorMatrix type="matrix" values="0 0 0 0 0.157483 0 0 0 0 0.804167 0 0 0 0 0.338554 0 0 0 0.19 0" />
            <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_30_362" />
            <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_30_362" result="shape" />
          </filter>
        </defs>
      </svg>

      <section className='signin--instruction'>
        <h1>Welcome Back!</h1>
        <p>sign in to your account</p>
      </section>

      <section className="signin--information">
        <input type="text" placeholder='Enter your email address' />
        <input type="text" placeholder='Enter your password' />
        <a href="">Forgot your password?</a>
        <button>Sign in</button>
      </section>

      <section className='signin--switch'>
        <p>Dont have an account? Let's</p>
        <a href="">Sign up</a>
      </section>

    </>
  )
}

export default App
