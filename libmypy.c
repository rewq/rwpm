#define _GNU_SOURCE
#include <stdlib.h>
#include <errno.h>
#include <sys/uio.h>
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "libmypy.h"


PyObject * method_process_vm_readv(PyObject *self, PyObject *args) {
	int pid;
	void* addr;
	size_t buf_size;
    char *buf;
    ssize_t nread;
	struct iovec local[1];
    struct iovec remote[1];
	PyObject *result;

	if(!PyArg_ParseTuple(args, "inn", &pid,&addr,&buf_size)) {
	    return NULL;
	}

	buf = (char *) PyMem_Malloc(buf_size); /* for I/O */

	if (buf == NULL){
		return PyErr_NoMemory();
	}
	

    local[0].iov_base = buf;
    local[0].iov_len = buf_size;
    remote[0].iov_base = addr;
    remote[0].iov_len = buf_size;

    nread = process_vm_readv(pid, local, 1, remote, 1, 0);

    if (nread == -1) {
        PyErr_SetFromErrno(PyExc_IOError);
    }

	result = PyBytes_FromStringAndSize(buf, buf_size);
	PyMem_Free(buf); /* allocated with PyMem_Malloc */
	return result;
}


PyObject * method_process_vm_writev(PyObject *self, PyObject *args) {
	int pid;
	void* addr;
    Py_buffer bytes;
    ssize_t nread;
	struct iovec local[1];
    struct iovec remote[1];
	//PyObject *result;

	if(!PyArg_ParseTuple(args, "iny*", &pid,&addr,&bytes)) {
	    return NULL;
	}
	
    local[0].iov_base = bytes.buf;
    local[0].iov_len = bytes.len;
    remote[0].iov_base = addr;
    remote[0].iov_len = bytes.len;

    nread = process_vm_writev(pid, local, 1, remote, 1, 0);

    if (nread == -1) {
        PyErr_SetFromErrno(PyExc_IOError);
    }

	return Py_BuildValue("l", nread);
}