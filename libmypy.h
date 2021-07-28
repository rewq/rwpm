#ifndef __LIBMYPY_H__
#define __LIBMYPY_H__

#include <Python.h>

PyObject * method_process_vm_readv(PyObject *self, PyObject *args);

PyObject * method_process_vm_writev(PyObject *self, PyObject *args);

#endif
