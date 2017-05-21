#include <Python.h>

PyObject * meth_quick_hull(PyObject * self, PyObject * args) {
	return 0;
}

PyMethodDef methods[] = {
	{"quick_hull", (PyCFunction)meth_quick_hull, METH_VARARGS, 0},
	{0},
};

#if PY_MAJOR_VERSION >= 3

PyModuleDef moduledef = {
	PyModuleDef_HEAD_INIT,
	"hull",
	0,
	-1,
	methods,
	0,
	0,
	0,
	0,
};

PyObject * InitializeGLWindow(PyObject * module) {
	return module;
}

extern "C" PyObject * PyInit_hull() {
	PyObject * module = PyModule_Create(&moduledef);
	return InitializeGLWindow(module);
}

#else

extern "C" PyObject * inithull() {
	PyObject * module = Py_InitModule("hull", methods);
	return InitializeGLWindow(module);
}

#endif
