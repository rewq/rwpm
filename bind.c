#include "libmypy.h"

char rwpmfunc_docs[] = "Hello world description.";

PyMethodDef rwpm_funcs[] = {
	{	"process_vm_readv",
		(PyCFunction)method_process_vm_readv,
		METH_VARARGS,
		rwpmfunc_docs},
	{	"process_vm_writev",
		(PyCFunction)method_process_vm_writev,
		METH_VARARGS,
		rwpmfunc_docs},
	{	NULL}
};

char rwpmmod_docs[] = "This is hello world module.";

PyModuleDef rwpm_mod = {
	PyModuleDef_HEAD_INIT,
	"rwpm",
	rwpmmod_docs,
	-1,
	rwpm_funcs,
	NULL,
	NULL,
	NULL,
	NULL
};

PyMODINIT_FUNC PyInit_rwpm(void) {
	return PyModule_Create(&rwpm_mod);
}
