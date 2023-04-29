import { createBrowserRouter, RouterProvider } from "react-router-dom";
import HomePage from "../Pages/HomePage";
import Form from "../Pages/FormPage/Form";

const Navigation = () => {
  const routes = [
    { path: "/", element: <HomePage /> },
    {path: '/form', element: <Form/>}
  ];

  const router = createBrowserRouter(routes);

  return <RouterProvider router={router} />;
};

export default Navigation;