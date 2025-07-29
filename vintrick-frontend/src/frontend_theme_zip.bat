@echo off
:: Run this script in vintrick-frontend\src

:: Create folder structure only if they don't exist
if not exist components\NavBar mkdir components\NavBar
if not exist components\Layout mkdir components\Layout
if not exist components\Button mkdir components\Button

:: Helper function to write content only if file doesn't exist
setlocal EnableDelayedExpansion

:: NavBar.jsx
if not exist components\NavBar\NavBar.jsx (
(
  echo import styles from './NavBar.module.css';
  echo import ^{ Link ^} from 'react-router-dom';
  echo.
  echo export default function NavBar() ^{
  echo   return (^<nav className=^"^${styles.nav}^"^>^<Link to=^"/^" className=^"^${styles.logo}^"^>Vintrick^</Link^>^<div className=^"^${styles.links}^"^>^<Link to=^"/harvestloads^"^>Harvest Loads^</Link^>^<Link to=^"/settings^"^>Settings^</Link^>^</div^>^</nav^>);
  echo ^}
) > components\NavBar\NavBar.jsx
)

:: NavBar.module.css
if not exist components\NavBar\NavBar.module.css (
(
  echo .nav {
  echo   display: flex;
  echo   justify-content: space-between;
  echo   align-items: center;
  echo   background-color: var(--color-primary);
  echo   padding: var(--space-md);
  echo   color: white;
  echo }
  echo.
  echo .logo {
  echo   font-size: var(--font-lg);
  echo   font-weight: bold;
  echo   color: white;
  echo   text-decoration: none;
  echo }
  echo.
  echo .links a {
  echo   margin-left: 1rem;
  echo   color: white;
  echo   text-decoration: none;
  echo }
) > components\NavBar\NavBar.module.css
)

:: Layout.jsx
if not exist components\Layout\Layout.jsx (
(
  echo import NavBar from '../NavBar/NavBar';
  echo import './Layout.css';
  echo.
  echo export default function Layout(^{
  echo   return (^<^>^<NavBar /^>^<main className=^"main^"^>^{{children}}^</main^>^</^>);
  echo ^}
) > components\Layout\Layout.jsx
)

:: Layout.css
if not exist components\Layout\Layout.css (
(
  echo .main {
  echo   padding: 1rem;
  echo   background-color: var(--color-bg);
  echo   min-height: 100vh;
  echo   font-family: Arial, sans-serif;
  echo }
) > components\Layout\Layout.css
)

:: Button.jsx
if not exist components\Button\Button.jsx (
(
  echo import styles from './Button.module.css';
  echo.
  echo export default function Button(^{
  echo   const classNames = [
  echo     styles.Button,
  echo     styles['Button--primary'],
  echo     styles['Button--medium']
  echo   ].join(' ');
  echo.
  echo   return (^<button className=^"^${classNames}^"^>^{children^}^</button^>);
  echo ^}
) > components\Button\Button.jsx
)

:: Button.module.css
if not exist components\Button\Button.module.css (
(
  echo .Button {
  echo   border: none;
  echo   border-radius: 4px;
  echo   cursor: pointer;
  echo   font-weight: 600;
  echo   padding: 0.5rem 1rem;
  echo   transition: background-color 0.3s ease;
  echo }
  echo.
  echo .Button--primary {
  echo   background-color: var(--color-primary);
  echo   color: white;
  echo }
  echo.
  echo .Button--secondary {
  echo   background-color: var(--color-secondary);
  echo   color: white;
  echo }
  echo.
  echo .Button--small {
  echo   font-size: 0.8rem;
  echo   padding: 0.25rem 0.5rem;
  echo }
  echo.
  echo .Button--medium {
  echo   font-size: 1rem;
  echo }
  echo.
  echo .Button--large {
  echo   font-size: 1.2rem;
  echo   padding: 0.75rem 1.5rem;
  echo }
) > components\Button\Button.module.css
)

echo ✅ Components created if they didn't already exist.
pause
