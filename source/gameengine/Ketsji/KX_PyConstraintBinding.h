/*
 * $Id: KX_PyConstraintBinding.h 35063 2011-02-22 10:33:14Z jesterking $
 *
 * ***** BEGIN GPL LICENSE BLOCK *****
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 * The Original Code is Copyright (C) 2001-2002 by NaN Holding BV.
 * All rights reserved.
 *
 * The Original Code is: all of this file.
 *
 * Contributor(s): none yet.
 *
 * ***** END GPL LICENSE BLOCK *****
 */

/** \file KX_PyConstraintBinding.h
 *  \ingroup ketsji
 */

#ifndef PHY_PYTHON_CONSTRAINTBINDING
#define PHY_PYTHON_CONSTRAINTBINDING

#ifdef WITH_PYTHON

#include <Python.h>

PyObject*				initPythonConstraintBinding();
void	PHY_RemovePythonConstraintBinding();
void	PHY_SetActiveEnvironment(class	PHY_IPhysicsEnvironment* env);
PHY_IPhysicsEnvironment*	PHY_GetActiveEnvironment();
#endif // WITH_PYTHON

#endif //PHY_PYTHON_CONSTRAINTBINDING

